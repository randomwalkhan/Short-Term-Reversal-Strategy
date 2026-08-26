# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 09:45:03 EDT`
Last processed slot: `manual`

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
- Equity: `$57,432.50`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$-270.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 28192.5        30.35          31.33      310.66        313.56          bid_ask_mid                      31.33                bid_ask_mid                    True           877.5                   3.21         87.50               32              1.06         63.04           63.11                  88.60                 214.0           30.0               0.05                      ok
   KHC     option         option  KHC261016C00025000       2026-08-25                   1    287     29274.0                 28126.0         1.02           0.98       25.19         25.07     last_price_stale                        NaN                unavailable                   False         -1148.0                  -3.92         86.67               15              1.85         24.46           15.43                  37.91                4031.0          107.0               0.04                      ok
```

## Today's Closed Trades (2026-08-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           89.47               19            0.96              0.33         48.59               552.32         1.000          pass              0.451             12.8                           0.210                4.96              0.587                      ok            True                  False
  ALNY           84.38               32            1.11              1.87        239.28               130.65         0.843          pass              0.420             24.1                           0.175                6.01              0.648                      ok            True                  False
  SHOP           90.62               32            1.56              1.68        153.16                72.08         0.616          pass              0.574             27.5                           0.233                0.71             -0.146                      ok            True                  False
  WDAY           80.56               36            1.24              1.69        193.70                76.21         0.605          pass              0.451             67.5                           0.788                9.54              0.316                      ok            True                  False
  REGN          100.00               20            1.18              6.89        830.61                29.20         0.568          pass              0.595             23.7                           0.209                3.34              0.446                      ok            True                  False
  DXCM           87.88               33            0.85              0.53         88.93                51.46         0.566          pass              0.583             54.2                           0.450               -2.64             -0.097                      ok            True                  False
   KHC           86.96               23            0.97              0.17         25.25                34.81         0.539          pass              0.557             77.1                           0.846                2.22              0.195                      ok            True                  False
  META           80.00               35            0.60              2.38        569.03                48.37         0.518          pass              0.392             58.0                           0.359               -2.11             -0.457                      ok            True                  False
  VRTX           96.77               31            0.96              3.72        551.26                33.40         0.515          pass              0.618              8.8                           0.270                4.15              0.781                      ok            True                  False
  PYPL           90.91               22            1.27              0.55         62.03                21.38         0.502          pass              0.432              3.7                           0.079                3.85              0.332                      ok            True                  False
  BKNG           97.22               36            0.75              1.13        213.30                35.36         0.501          pass              0.715             30.6                           0.271               -0.04              0.072                      ok            True                  False
  INSM           86.84               38            1.00              0.86        123.52               110.58         0.693          pass              0.667             76.2                           0.334               -7.28             -0.470 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                  detail
2026-08-26T00:00:04.646772-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                                           {'saved': 93}
2026-08-25T15:10:01.918364-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T15:05:01.097664-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T15:00:03.828348-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T14:55:05.864506-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped            {"early_entry_score": 0.306, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.47, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.567}
2026-08-25T14:50:01.861538-04:00   entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-25", "training_samples": 5700, "window": 5}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped                                  {"early_entry_score": 0.418, "option_liquidity_status": "low_volume", "option_open_interest": 249.0, "option_spread_pct": 6.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MNST", "timing_score": 1.0}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.342, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 85.0, "option_spread_pct": 14.43, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "DXCM", "timing_score": 0.569}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped              {"early_entry_score": 0.471, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 11.32, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.558}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826094503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826094503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826094503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826094503)

</details>
