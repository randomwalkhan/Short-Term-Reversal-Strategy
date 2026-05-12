# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 11:20:04 EDT`
Last processed slot: `manage_1130`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260618C00520000      5          2026-05-12         2026-05-12         35.0        31.5 -1750.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           86.84               38            1.31              0.80         86.97               115.89         0.700          pass              0.582             47.7                           0.359               23.61              2.546                                 ok            True                  False
  FTNT           93.75               32            1.12              0.90        115.05                70.54         0.598          pass              0.656             27.5                           0.194               33.17              3.598                                 ok            True                  False
   XEL           92.86               14            1.14              0.64         80.32                27.14         0.539          pass              0.615             63.8                           0.379                0.25             -0.079                                 ok            True                  False
    ZS           82.86               35            0.95              0.99        148.45                59.15         0.537          pass              0.440             47.8                           0.385                8.37              1.277                                 ok            True                  False
   CSX           82.61               23            1.04              0.33         44.60                30.07         0.530          pass              0.238              9.7                           0.260               -2.11             -0.136                                 ok            True                  False
  CDNS           95.45               22            2.05              5.22        361.96                37.36         0.523          pass              0.561              9.7                           0.194                9.66              1.135                                 ok            True                  False
  MNST           86.49               37            0.52              0.32         86.27                49.64         0.511          pass              0.657             84.2                           0.630               11.36              1.212                                 ok            True                  False
  CHTR           89.13               46            0.29              0.30        147.66               118.46         0.777          pass              0.750             76.3                           0.426              -14.87             -1.356            downtrend_blocked_slope           False                  False
   TXN           80.00                5            2.99              6.24        295.09                67.69         0.675          pass              0.079              3.8                           0.215                9.55              0.923                                 ok           False                  False
 CMCSA           93.94               33            0.22              0.04         25.01                62.25         0.667          pass              0.820             76.1                           0.603               -9.64             -0.970 downtrend_blocked_slope_and_streak           False                  False
  SHOP           89.74               39            0.96              0.69        102.24                84.99         0.647          pass              0.584             22.0                           0.184              -16.79             -2.113            downtrend_blocked_slope           False                  False
  NXPI           50.00                2            4.49              9.61        301.87                87.21         0.591          pass              0.188             43.0                           0.256               26.85              1.286                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                           detail
2026-05-12T11:20:04.203525-04:00 early_entry_1120 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T11:15:02.113250-04:00 early_entry_1115 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T11:10:01.083696-04:00 early_entry_1110 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T11:05:04.072050-04:00 early_entry_1105 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T11:00:02.153694-04:00 early_entry_1100 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:55:01.118172-04:00 early_entry_1055 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:50:05.198846-04:00 early_entry_1050 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:45:04.189034-04:00 early_entry_1045 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:40:01.090615-04:00 early_entry_1040 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00520000", "fill_price": 31.5, "pnl": -1750.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512112004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512112004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512112004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512112004)

</details>
