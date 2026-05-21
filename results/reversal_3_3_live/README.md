# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 12:35:01 EDT`
Last processed slot: `manage_1230`

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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$16,177.75`
- Equity: `$28,757.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$440.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   0      4     12140.0                 12580.0        30.35          31.45      415.18        413.38          bid_ask_mid                      31.45                bid_ask_mid                    True           440.0                   3.62         91.67               36              0.62         50.17           52.32                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  INTC           96.67               30            1.42              1.19        118.45               113.85         0.719          pass              0.817             70.7                           0.571                6.97             -0.585                      ok            True                   True
  FTNT          100.00               27            1.30              1.18        129.49                70.74         0.651          pass              0.695             39.0                           0.356               18.84              1.764                      ok            True                  False
  PAYX           93.75               16            0.81              0.54         94.69                29.35         0.565          pass              0.656             64.4                           0.371                1.17              0.244                      ok            True                  False
  MNST           80.00               25            1.13              0.69         86.59                49.77         0.557          pass              0.390             78.0                           0.451               13.07              0.649                      ok            True                  False
  AMAT           82.35               34            0.77              2.29        425.87                55.19         0.546          pass              0.423             48.7                           0.378                3.15             -0.243                      ok            True                  False
  FAST           93.33               15            1.30              0.40         43.51                21.35         0.538          pass              0.521             26.0                           0.289               -2.82             -0.136                      ok            True                  False
   ADP           93.75               32            0.70              1.09        220.22                38.26         0.529          pass              0.752             61.9                           0.487                2.36              0.447                      ok            True                  False
  NVDA           85.71               21            1.71              2.68        222.32                44.60         0.521          pass              0.370             30.9                           0.362                3.85              0.334                      ok            True                  False
  ISRG           90.91               11            2.49              7.83        445.67                35.82         0.519          pass              0.408             19.4                           0.462               -3.45             -0.022                      ok            True                  False
    ZS           82.35               17            2.53              3.09        173.13                63.59         0.516          pass              0.223             20.7                           0.370               11.29              1.803                      ok            True                  False
  SOXL           84.38               32            0.03              0.04        173.18               145.82         0.806          pass              0.641             98.9                           0.640               13.83             -0.443                      ok           False                  False
  CHTR           88.37               43            0.35              0.36        144.46               113.96         0.762          pass              0.744             81.5                           0.665              -10.07             -0.933 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-21T12:00:02.068266-04:00 early_entry_1200           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T11:55:01.035616-04:00 early_entry_1155           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T11:50:01.038543-04:00 early_entry_1150                   entry {"allocated_cash": 12140.0, "asset_type": "option", "contract_symbol": "AVGO260717C00420000", "contracts": 4, "early_entry_score": 0.724, "entry_mode": "early", "entry_option_price": 30.35, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2101.0, "option_spread_pct": 2.97, "option_volume": 296.0, "success_rate": 91.67, "ticker": "AVGO", "timing_score": 0.497}
2026-05-21T11:45:04.222670-04:00 early_entry_1145           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-05-21T11:40:04.207622-04:00 early_entry_1140           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:40:04.207622-04:00 early_entry_1140 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.775, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 7.04, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T11:35:02.090762-04:00 early_entry_1135           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-05-21T11:30:02.245220-04:00 early_entry_1130           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 6.12, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521123501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521123501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521123501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521123501)

</details>
