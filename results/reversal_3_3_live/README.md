# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 10:40:01 EDT`
Last processed slot: `manage_1030`

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
  TEAM           87.50               40            1.07              0.65         87.03               115.89         0.703          pass              0.642             57.3                           0.447               23.91              2.558                                 ok            True                  False
   TXN           91.67               12            2.10              4.37        295.89                67.69         0.698          pass              0.473             26.4                           0.348               10.57              0.965                                 ok            True                  False
  GOOG           89.47               38            0.53              1.43        386.16                39.86         0.539          pass              0.662             56.3                           0.677               10.71              1.056                                 ok            True                  False
   XEL           93.33               15            1.12              0.63         80.33                27.14         0.535          pass              0.636             64.6                           0.507                0.28             -0.078                                 ok            True                  False
    ZS           81.58               38            0.72              0.75        148.55                59.15         0.530          pass              0.463             60.6                           0.640                8.62              1.288                                 ok            True                  False
   CSX           84.00               25            0.98              0.31         44.61                30.07         0.523          pass              0.303             14.6                           0.261               -2.06             -0.134                                 ok            True                  False
  CDNS           96.43               28            1.48              3.76        362.59                37.36         0.521          pass              0.644             24.1                           0.305               10.30              1.162                                 ok            True                  False
  MNST           85.71               35            0.61              0.37         86.25                49.64         0.516          pass              0.615             81.6                           0.748               11.26              1.208                                 ok            True                  False
 CMCSA           92.31               26            0.58              0.10         24.99                62.25         0.683          pass              0.614             37.0                           0.361               -9.97             -0.986 downtrend_blocked_slope_and_streak           False                  False
  SHOP           90.91               44            0.20              0.14        102.48                84.99         0.662          pass              0.810             84.2                           0.662              -16.15             -2.078            downtrend_blocked_slope           False                  False
  NXPI           64.29               14            3.06              6.55        303.18                87.21         0.617          pass              0.272             61.2                           0.427               28.75              1.354                                 ok           False                  False
  FTNT           95.45               44            0.38              0.31        115.31                70.54         0.572          pass              0.883             75.3                           0.700               34.16              3.632                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-12T10:40:01.090615-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00      manage_1030          exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "SNPS260618C00520000", "fill_price": 31.5, "pnl": -1750.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-12T10:30:01.090620-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:25:01.082139-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:20:02.261414-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:15:01.147250-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:10:05.279382-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:05:06.121865-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:00:05.800159-04:00 early_entry_1000         entry {"allocated_cash": 17500.0, "asset_type": "option", "contract_symbol": "SNPS260618C00520000", "contracts": 5, "early_entry_score": 0.854, "entry_mode": "early", "entry_option_price": 35.0, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 202.0, "option_spread_pct": 0.0, "option_volume": 13.0, "success_rate": 96.97, "ticker": "SNPS", "timing_score": 0.483}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512104001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512104001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512104001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512104001)

</details>
