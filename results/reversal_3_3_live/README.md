# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 11:15:02 EDT`
Last processed slot: `early_entry_1115`

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
  TEAM           87.50               40            1.18              0.72         87.00               115.89         0.697          pass              0.628             52.8                           0.380               23.77              2.552                                 ok            True                  False
  FTNT           94.74               38            0.75              0.61        115.18                70.54         0.585          pass              0.792             51.1                           0.340               33.66              3.615                                 ok            True                  False
  GOOG           89.47               38            0.54              1.45        386.15                39.86         0.539          pass              0.661             55.9                           0.650               10.71              1.056                                 ok            True                  False
   XEL           92.86               14            1.15              0.65         80.32                27.14         0.539          pass              0.614             63.6                           0.381                0.25             -0.079                                 ok            True                  False
    ZS           83.33               36            0.88              0.92        148.48                59.15         0.535          pass              0.470             51.5                           0.436                8.44              1.280                                 ok            True                  False
  CDNS           96.00               25            1.80              4.59        362.23                37.36         0.522          pass              0.575              7.5                           0.135                9.94              1.147                                 ok            True                  False
   CSX           85.19               27            0.89              0.28         44.62                30.07         0.518          pass              0.370             22.3                           0.390               -1.97             -0.130                                 ok            True                  False
  CHTR           88.64               44            0.38              0.39        147.62               118.46         0.781          pass              0.715             68.9                           0.334              -14.95             -1.361            downtrend_blocked_slope           False                  False
   TXN           87.50                8            2.76              5.75        295.30                67.69         0.683          pass              0.278              3.2                           0.137                9.82              0.934                                 ok           False                  False
 CMCSA           94.12               34            0.18              0.03         25.02                62.25         0.664          pass              0.844             80.4                           0.571               -9.61             -0.968 downtrend_blocked_slope_and_streak           False                  False
  SHOP           90.24               41            0.69              0.49        102.33                84.99         0.651          pass              0.671             44.2                           0.282              -16.56             -2.100            downtrend_blocked_slope           False                  False
  NXPI           50.00                2            4.45              9.54        301.90                87.21         0.592          pass              0.190             43.4                           0.258               26.90              1.288                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                           detail
2026-05-12T11:15:02.113250-04:00 early_entry_1115 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T11:10:01.083696-04:00 early_entry_1110 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T11:05:04.072050-04:00 early_entry_1105 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T11:00:02.153694-04:00 early_entry_1100 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:55:01.118172-04:00 early_entry_1055 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:50:05.198846-04:00 early_entry_1050 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:45:04.189034-04:00 early_entry_1045 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:40:01.090615-04:00 early_entry_1040 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00 early_entry_1035 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00520000", "fill_price": 31.5, "pnl": -1750.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512111502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512111502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512111502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512111502)

</details>
