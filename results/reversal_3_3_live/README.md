# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 10:45:05 EDT`
Last processed slot: `early_entry_1045`

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
- Equity: `$26,742.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$280.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 12635.0         8.82           9.02      126.75        127.56          bid_ask_mid                       9.02                bid_ask_mid                    True           280.0                   2.27         100.0               38              0.69         41.39           39.93                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           90.91               11            1.39              1.30        133.64                20.68         0.533            pass              0.528             58.9                           0.720                1.93              0.333                                 ok            True                  False
  ADSK           90.91               22            1.37              2.34        243.16                38.52         0.510            pass              0.630             69.5                           0.699               -0.93             -0.154                                 ok            True                  False
 GOOGL           87.88               33            0.72              1.97        386.82                41.27         0.504            pass              0.537             41.0                           0.323               -3.31             -0.206                                 ok            True                  False
  AMGN           84.00               25            0.53              1.22        330.23                26.77         0.501            pass              0.502             81.9                           0.554                0.11              0.006                                 ok            True                  False
  TMUS           82.61               23            1.48              2.00        192.56                36.70         0.500            pass              0.255             16.4                           0.116               -1.35             -0.197                                 ok            True                  False
  FTNT          100.00               48            0.03              0.02        127.63                70.74         0.598            pass              0.955             98.5                           0.836               41.86              2.654                                 ok           False                  False
  TEAM           87.88               33            2.21              1.34         86.05               114.61         0.598            pass              0.594             56.8                           0.479               -4.61             -0.556 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.00               20            0.38              0.25         94.37                29.36         0.562            pass              0.787             88.0                           0.787                4.32              0.239                                 ok           False                  False
  CTSH           86.96               23            1.33              0.47         50.68                50.98         0.517            pass              0.520             65.5                           0.692               -1.50             -0.226           downtrend_blocked_streak           False                  False
  SNPS           97.22               36            0.50              1.71        493.14                41.71         0.495 below_threshold              0.886             87.8                           0.869               -2.58             -0.353 downtrend_blocked_slope_and_streak           False                  False
   KDP           89.47               38            0.21              0.04         28.83                34.80         0.495 below_threshold              0.755             88.6                           0.752                0.81              0.146                                 ok           False                  False
  GOOG           87.88               33            0.73              1.96        384.06                41.08         0.493 below_threshold              0.541             42.7                           0.338               -3.30             -0.215           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-20T10:45:05.974600-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:40:03.515008-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:35:01.049335-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:30:01.058983-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:25:06.944713-04:00 early_entry_1025                   entry {"allocated_cash": 12355.0, "asset_type": "option", "contract_symbol": "FTNT260717C00125000", "contracts": 14, "early_entry_score": 0.837, "entry_mode": "early", "entry_option_price": 8.825, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 1300.0, "option_spread_pct": 11.9, "option_volume": 40.0, "success_rate": 100.0, "ticker": "FTNT", "timing_score": 0.622}
2026-05-20T10:21:54.079183-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.683, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 46.51, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTAS", "timing_score": 0.458}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                                         {"early_entry_score": 0.801, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 29.0, "option_spread_pct": 26.59, "option_volume": 20.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.484}
2026-05-20T10:05:07.673831-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-05-20T10:03:13.062601-04:00 early_entry_1000 entry_candidate_skipped                                                                                                                                                       {"early_entry_score": 0.801, "option_liquidity_status": "low_open_interest,no_two_sided_quote,wide_spread", "option_open_interest": 29.0, "option_spread_pct": null, "option_volume": 20.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.484}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520104505)

</details>
