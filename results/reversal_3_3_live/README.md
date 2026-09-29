# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 09:55:06 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$35,438.30`
- Equity: `$71,798.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$1,800.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-09-28                   1     24     34560.0                 36360.0         14.4          15.15      261.15        267.73          bid_ask_mid                      15.15                bid_ask_mid                    True          1800.0                   5.21         89.66               29              0.81          46.4           43.37                   41.9                 366.0           20.0               0.04                      ok
```

## Today's Closed Trades (2026-09-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    ZS           97.56               41            0.70              0.97        198.97                81.58         0.593          pass              0.862             67.5                           0.446                2.12              0.364                      ok            True                  False
   BKR           88.24               17            1.35              0.54         56.89                32.18         0.509          pass              0.507             63.3                           0.547               -0.65              0.086                      ok            True                  False
  ALNY           82.50               40            0.72              1.29        254.81                45.92         0.502          pass              0.394             25.8                           0.338                6.40              0.714                      ok            True                  False
   TRI           88.24               34            0.79              0.54         97.10                56.59         0.577          pass              0.620             60.8                           0.625               -5.89             -0.296 downtrend_blocked_slope           False                  False
  CRWD           89.13               46            0.49              0.90        258.87                71.98         0.575          pass              0.691             63.3                           0.427                6.38              0.820                      ok           False                  False
   WBD           95.00               40            0.15              0.03         30.89                38.06         0.574          pass              0.842             61.5                           0.370               10.08              1.215                      ok           False                  False
  AMGN           87.18               39            0.15              0.45        417.94                46.33         0.570          pass              0.700             86.2                           0.642               11.14              1.225                      ok           False                  False
  TMUS           81.82               22            1.07              1.25        165.91                33.31         0.536          pass              0.291             36.5                           0.464               -8.76             -0.670 downtrend_blocked_slope           False                  False
   STX           88.57               35            0.46              2.94        920.25                53.46         0.535          pass              0.666             72.3                           0.420               18.95              1.892                      ok           False                  False
  QCOM           92.50               40            0.05              0.06        187.45                57.69         0.533          pass              0.867             93.4                           0.453               -0.22              0.403                      ok           False                  False
  PANW           63.16               19            3.05              8.36        388.51                69.78         0.527          pass              0.159             15.4                           0.206                1.35              0.393                      ok           False                  False
  CDNS           70.59               17            2.31              5.28        324.44                46.51         0.511          pass              0.220             40.6                           0.445               16.50              1.943                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-29T00:00:05.209830-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-28T15:10:04.000540-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-28T15:05:05.114052-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-28T15:00:06.099119-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-28T14:55:04.074412-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-28T14:50:04.136803-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 34560.0, "asset_type": "option", "contract_symbol": "CEG261120C00270000", "contracts": 24, "early_entry_score": 0.63, "entry_mode": "regular", "entry_option_price": 14.4, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 366.0, "option_spread_pct": 4.17, "option_volume": 20.0, "success_rate": 89.66, "ticker": "CEG", "timing_score": 0.542}
2026-09-28T14:50:04.136803-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-28", "training_samples": 5994, "window": 5}
2026-09-28T12:00:07.024087-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.61, "early_entry_score": 0.741, "early_reclaim_pct": 78.2, "entry_ask": 30.4, "entry_bid": 29.1, "entry_mode": "early", "entry_option_price": 29.75, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 4.37, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.704, "shadow_only": true, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.741, "early_reclaim_pct": 78.2, "matched_signals": 34, "recovery_stability_score": 0.704, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.483, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:55:06.078627-04:00 early_entry_1155 early_entry_shadow  {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.67, "early_entry_score": 0.721, "early_reclaim_pct": 76.0, "entry_ask": 30.9, "entry_bid": 29.7, "entry_mode": "early", "entry_option_price": 30.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 3.96, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.721, "early_reclaim_pct": 76.0, "matched_signals": 33, "recovery_stability_score": 0.676, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.484, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:50:06.060997-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929095506)

</details>
