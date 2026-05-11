# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 11:22:14 EDT`
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

- Cash: `$35,353.50`
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG260618C00290000      7          2026-05-11         2026-05-11         23.2        26.8 2520.0   15.517241 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  GOOG           81.82               11            1.78              4.94        394.94                37.66         0.600          pass              0.162             15.5                           0.226               11.90              1.413                                 ok            True                  False
  TEAM           81.82               11            5.32              3.41         90.14               114.36         0.596          pass              0.155             13.4                           0.371               25.30              3.260                                 ok            True                  False
  MNST           80.00               20            1.19              0.72         86.00                49.83         0.541          pass              0.319             66.2                           0.652               10.95              0.832                                 ok            True                  False
  SNPS           97.30               37            0.52              1.89        515.67                46.53         0.537          pass              0.850             72.1                           0.407                3.06              0.612                                 ok            True                  False
    ZS           80.00               20            2.55              2.72        150.97                58.64         0.528          pass              0.159             13.2                           0.247               10.54              1.324                                 ok            True                  False
   ADP           93.33               30            0.66              0.99        212.57                34.95         0.515          pass              0.740             66.5                           0.349                7.28              0.494                                 ok            True                  False
  TMUS           85.71               35            0.64              0.86        193.26                36.59         0.513          pass              0.535             54.8                           0.542                5.28              0.281                                 ok            True                  False
   WMT           81.82               11            1.79              1.64        129.73                19.38         0.513          pass              0.116              3.3                           0.159                0.58              0.128                                 ok            True                  False
  CHTR           78.57               14            2.84              3.08        153.54               119.48         0.778          pass              0.175             23.6                           0.280              -13.83             -1.227            downtrend_blocked_slope           False                  False
  NXPI           82.05               39            0.25              0.51        294.53                87.07         0.708          pass              0.560             80.5                           0.579               24.13              1.939                                 ok           False                  False
 CMCSA           90.91               22            0.71              0.13         25.34                62.19         0.695          pass              0.537             32.1                           0.385               -8.34             -0.822 downtrend_blocked_slope_and_streak           False                  False
  FTNT           95.56               45            0.41              0.33        113.93                70.49         0.579          pass              0.906             82.8                           0.466               32.60              3.094                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                               detail
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:56:33.081827-04:00 early_entry_1055 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:50:08.671190-04:00 early_entry_1050 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:43:44.045089-04:00 early_entry_1040 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "CEG260618C00290000", "fill_price": 26.8, "pnl": 2520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.52, "ticker": "CEG"}
2026-05-11T10:37:19.097633-04:00 early_entry_1035 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-11T10:30:53.059924-04:00 early_entry_1030 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511112214)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511112214)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511112214)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511112214)

</details>
