# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 15:10:04 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$13,462.50`
- Equity: `$26,722.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$208.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option WMT260724C00120000       2026-06-18                   0     52     13052.0                 13260.0         2.51           2.55      117.33        117.16          bid_ask_mid                       2.55                bid_ask_mid                    True           208.0                   1.59         86.21               29              0.68         25.57           26.73                  34.58                 124.0           47.0               0.14                      ok
```

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           84.62               26            0.82              0.68        117.84                34.58         0.559          pass              0.368             27.3                           0.355               -0.49              0.015                                 ok            True                  False
  CRWD           86.11               36            0.77              3.66        681.39                64.33         0.544          pass              0.620             76.3                           0.425               -5.75              0.058                                 ok            True                  False
  MDLZ           95.24               21            0.97              0.41         60.68                21.28         0.518          pass              0.626             33.7                           0.475               -1.18             -0.158                                 ok            True                  False
   XEL          100.00               15            0.70              0.38         77.30                22.61         0.518          pass              0.498              4.4                           0.071               -0.35              0.067                                 ok            True                  False
  VRTX           94.74               19            1.35              4.34        457.13                24.55         0.501          pass              0.586             27.5                           0.274                2.50              0.310                                 ok            True                  False
    ZS           79.55               44            0.01              0.01        124.38               152.31         0.879          pass              0.587             99.8                           0.652               -8.05             -0.508 downtrend_blocked_slope_and_streak           False                  False
  INTU           73.33               30            1.58              2.98        267.80                98.62         0.688          pass              0.372             56.8                           0.527              -12.31             -1.281 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                2            1.40              0.23         23.10                27.50         0.667          pass              0.477              3.3                           0.200                3.65              0.369                                 ok           False                  False
   PEP          100.00               19            0.24              0.24        141.49                22.29         0.617          pass              0.649             42.4                           0.306                0.41              0.157                                 ok           False                  False
   TRI           77.27               22            1.38              0.76         78.92                52.51         0.569          pass              0.286             49.8                           0.433               -8.84             -0.834 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            2.05              4.90        339.56                27.62         0.555          pass              0.168              8.0                           0.261               -3.17             -0.136           downtrend_blocked_streak           False                  False
  TEAM           86.11               36            1.32              0.78         84.06                82.55         0.549          pass              0.564             57.4                           0.327              -17.96             -1.899 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-18T15:10:04.271531-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-18T15:05:02.244288-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-18T15:00:03.400898-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-18T14:55:03.329967-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-18T14:50:01.395672-04:00       entry_1500              entry {"allocated_cash": 13052.0, "asset_type": "option", "contract_symbol": "WMT260724C00120000", "contracts": 52, "early_entry_score": 0.467, "entry_mode": "regular", "entry_option_price": 2.51, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 124.0, "option_spread_pct": 13.55, "option_volume": 47.0, "success_rate": 86.21, "ticker": "WMT", "timing_score": 0.549}
2026-06-18T14:50:01.395672-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-18", "training_samples": 5252, "window": 5}
2026-06-18T12:00:02.352957-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:55:04.331586-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:50:03.235877-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:45:01.152442-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618151004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618151004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618151004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618151004)

</details>
