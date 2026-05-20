# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 10:25:06 EDT`
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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$14,107.75`
- Equity: `$26,462.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 12355.0         8.82           8.82      126.75        126.98          bid_ask_mid                       8.82                bid_ask_mid                    True             0.0                    0.0         100.0               38              0.69         41.39           41.39                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               38            0.69              0.62        127.37                70.74         0.622            pass              0.837             62.7                           0.684               40.92              2.623                                 ok            True                   True
  PAYX           94.44               18            0.56              0.37         94.32                29.36         0.563            pass              0.742             82.4                           0.788                4.13              0.231                                 ok            True                  False
   KDP           89.66               29            0.69              0.14         28.79                34.80         0.524            pass              0.622             61.9                           0.329                0.32              0.124                                 ok            True                  False
  ADSK           86.67               15            1.85              3.16        242.80                38.52         0.520            pass              0.439             58.8                           0.723               -1.42             -0.177                                 ok            True                  False
   TXN           94.12               34            0.01              0.03        302.30                69.06         0.643            pass              0.900             99.7                           0.535                4.43              0.596                                 ok           False                  False
  TEAM           87.88               33            2.09              1.27         86.08               114.61         0.605            pass              0.601             59.0                           0.647               -4.49             -0.550 downtrend_blocked_slope_and_streak           False                  False
  CTSH           83.33               18            1.63              0.58         50.63                50.98         0.525            pass              0.367             57.5                           0.667               -1.81             -0.241           downtrend_blocked_streak           False                  False
   WMT           88.89                9            1.76              1.65        133.49                20.68         0.519            pass              0.433             47.9                           0.348                1.55              0.316                                 ok           False                  False
 GOOGL           88.89               36            0.53              1.44        387.04                41.27         0.498 below_threshold              0.630             56.7                           0.411               -3.13             -0.197                                 ok           False                  False
  TMUS           86.21               29            1.02              1.38        192.83                36.70         0.495 below_threshold              0.469             42.4                           0.254               -0.89             -0.176                                 ok           False                  False
  SNPS           96.30               27            1.41              4.88        491.78                41.71         0.494 below_threshold              0.758             65.3                           0.744               -3.47             -0.395 downtrend_blocked_slope_and_streak           False                  False
  MSFT           82.61               23            1.17              3.41        415.96                29.51         0.490 below_threshold              0.266             20.3                           0.289               -0.34              0.054                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-20T10:25:06.944713-04:00 early_entry_1025                   entry {"allocated_cash": 12355.0, "asset_type": "option", "contract_symbol": "FTNT260717C00125000", "contracts": 14, "early_entry_score": 0.837, "entry_mode": "early", "entry_option_price": 8.825, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 1300.0, "option_spread_pct": 11.9, "option_volume": 40.0, "success_rate": 100.0, "ticker": "FTNT", "timing_score": 0.622}
2026-05-20T10:21:54.079183-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.683, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 46.51, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTAS", "timing_score": 0.458}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                                         {"early_entry_score": 0.801, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 29.0, "option_spread_pct": 26.59, "option_volume": 20.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.484}
2026-05-20T10:05:07.673831-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-05-20T10:03:13.062601-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-20T10:03:13.062601-04:00 early_entry_1000 entry_candidate_skipped                                                                                                                                                       {"early_entry_score": 0.801, "option_liquidity_status": "low_open_interest,no_two_sided_quote,wide_spread", "option_open_interest": 29.0, "option_spread_pct": null, "option_volume": 20.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.484}
2026-05-20T10:03:13.062601-04:00 early_entry_1000 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.821, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 15.38, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "TTWO", "timing_score": 0.44}
2026-05-20T09:18:59.431991-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92}
2026-05-19T15:10:04.056831-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520102506)

</details>
