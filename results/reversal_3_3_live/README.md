# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-15 15:25:04 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$14,083.25`
- Equity: `$26,503.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$-805.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ROST     option         option ROST260717C00240000       2026-06-15                   0     23     13225.0                 12420.0         5.75            5.4      236.66        236.55          bid_ask_mid                        5.4                bid_ask_mid                    True          -805.0                  -6.09         91.67               12              1.45         26.78           25.59                  38.75                 169.0           31.0               0.12                      ok
```

## Today's Closed Trades (2026-06-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ROST           91.67               12            1.49              2.51        239.06                38.75         0.619          pass              0.436             16.6                           0.248                5.78              0.608                                 ok            True                  False
  CPRT           84.62               13            2.07              0.44         30.56                31.00         0.526          pass              0.207              3.8                           0.177               -6.82             -0.226                                 ok            True                  False
   BKR           81.82               33            0.83              0.37         62.98                39.91         0.513          pass              0.460             69.0                           0.612               -0.56             -0.202                                 ok            True                  False
  CTAS           96.00               25            1.09              1.34        175.71                29.28         0.505          pass              0.651             33.5                           0.414                0.85              0.235                                 ok            True                  False
  ORLY           82.35               17            1.37              0.88         90.64                22.89         0.503          pass              0.274             38.1                           0.410                3.61              0.436                                 ok            True                  False
   KHC          100.00                3            1.13              0.19         24.31                26.17         0.664          pass              0.516             16.7                           0.390                3.90              0.779                                 ok           False                  False
   TRI           80.00               25            0.72              0.41         81.23                63.37         0.641          pass              0.237             24.4                           0.390              -13.98             -1.158 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               27            0.04              0.03        100.62                32.56         0.578          pass              0.840             89.5                           0.499               -1.81             -0.040                                 ok           False                  False
  WDAY           84.85               33            1.23              1.13        130.32                70.45         0.553          pass              0.417             26.2                           0.402              -17.83             -1.899 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.00               20            1.60              2.53        225.13                32.50         0.549          pass              0.542              6.7                           0.202               -4.77             -0.320            downtrend_blocked_slope           False                  False
  MDLZ           80.00                5            1.98              0.87         62.62                19.17         0.544          pass              0.119             21.6                           0.510                1.13              0.351                                 ok           False                  False
 CMCSA           75.00               12            1.59              0.27         24.38                24.55         0.529          pass              0.100             11.4                           0.410               -3.75             -0.139                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et       slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-15T15:10:06.131512-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T15:05:05.449965-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T15:00:05.161177-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T14:55:01.106139-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T14:50:01.113692-04:00 entry_1500          entry {"allocated_cash": 13225.0, "asset_type": "option", "contract_symbol": "ROST260717C00240000", "contracts": 23, "early_entry_score": 0.444, "entry_mode": "regular", "entry_option_price": 5.75, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 12.17, "option_volume": 31.0, "success_rate": 91.67, "ticker": "ROST", "timing_score": 0.621}
2026-06-15T14:50:01.113692-04:00 entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-15", "training_samples": 5261, "window": 5}
2026-06-12T15:10:11.830500-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T15:05:11.809096-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T15:00:11.776390-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T14:55:11.337200-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260615152504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260615152504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260615152504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260615152504)

</details>
