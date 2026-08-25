# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 16:00:02 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$1,114.00`
- Equity: `$58,057.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$354.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 28530.0        30.35          31.70      310.66        314.80          bid_ask_mid                      31.70                bid_ask_mid                    True          1215.0                   4.45         87.50               32              1.06         63.04           61.87                  88.60                 214.0           30.0               0.05                      ok
   KHC     option         option  KHC261016C00025000       2026-08-25                   0    287     29274.0                 28413.0         1.02           0.99       25.19         25.32          bid_ask_mid                       0.99                bid_ask_mid                    True          -861.0                  -2.94         86.67               15              1.85         24.46           21.97                  37.91                4031.0          107.0               0.04                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           88.00               25            2.97              4.14        197.38                78.88         0.557          pass              0.381              3.9                           0.199                6.60              0.690                                 ok            True                  False
   KHC           85.00               20            1.38              0.25         25.56                37.91         0.552          pass              0.338             27.6                           0.511                2.70              0.345                                 ok            True                  False
   MAR           96.55               29            0.67              1.70        359.47                33.78         0.547          pass              0.776             64.8                           0.452                2.58              0.227                                 ok            True                  False
  PAYX          100.00               23            0.82              0.72        125.70                34.31         0.545          pass              0.684             47.7                           0.338                3.03              0.325                                 ok            True                  False
  COST           93.75               16            1.17              7.97        967.98                19.15         0.528          pass              0.463              1.0                           0.108                1.66              0.068                                 ok            True                  False
   KDP           84.62               13            2.11              0.48         32.30                31.66         0.518          pass              0.211              5.5                           0.286                9.06              0.856                                 ok            True                  False
  MNST           94.29               35            0.43              0.15         48.86               552.55         1.000          pass              0.839             63.8                           0.584                6.98              0.660                                 ok           False                  False
  INSM           87.50               48            0.10              0.08        123.94               110.65         0.771          pass              0.745             89.2                           0.493               -6.57             -0.521            downtrend_blocked_slope           False                  False
  TEAM           76.92               26            2.82              3.39        169.88               115.46         0.725          pass              0.246             22.3                           0.442                8.05              1.029                                 ok           False                  False
  AMAT           90.62               32            0.86              2.90        482.95                81.86         0.658          pass              0.646             50.2                           0.565               -8.57             -1.183            downtrend_blocked_slope           False                  False
  MCHP           87.88               33            0.96              0.50         74.00                69.73         0.625          pass              0.529             34.3                           0.378               -8.74             -0.814            downtrend_blocked_slope           False                  False
  AMZN           75.61               41            0.42              0.77        261.74                59.56         0.595          pass              0.412             50.9                           0.561               -4.15             -0.334 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et       slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-25T15:10:01.918364-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-25T15:05:01.097664-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-25T15:00:03.828348-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-25T14:55:05.864506-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-25T14:50:01.861538-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                          {"early_entry_score": 0.306, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.47, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.567}
2026-08-25T14:50:01.861538-04:00 entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-25", "training_samples": 5700, "window": 5}
2026-08-25T14:50:01.861538-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.342, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 85.0, "option_spread_pct": 14.43, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "DXCM", "timing_score": 0.569}
2026-08-25T14:50:01.861538-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                                                {"early_entry_score": 0.418, "option_liquidity_status": "low_volume", "option_open_interest": 249.0, "option_spread_pct": 6.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MNST", "timing_score": 1.0}
2026-08-25T14:50:01.861538-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.471, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 11.32, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.558}
2026-08-25T14:50:01.861538-04:00 entry_1500                   entry {"allocated_cash": 29274.0, "asset_type": "option", "contract_symbol": "KHC261016C00025000", "contracts": 287, "early_entry_score": 0.276, "entry_mode": "regular", "entry_option_price": 1.02, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 4031.0, "option_spread_pct": 3.92, "option_volume": 107.0, "success_rate": 86.67, "ticker": "KHC", "timing_score": 0.558}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825160002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825160002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825160002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825160002)

</details>
