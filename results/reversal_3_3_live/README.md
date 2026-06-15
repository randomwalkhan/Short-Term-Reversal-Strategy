# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-15 16:00:05 EDT`
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

- Cash: `$14,083.25`
- Equity: `$26,273.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$-1,035.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ROST     option         option ROST260717C00240000       2026-06-15                   0     23     13225.0                 12190.0         5.75            5.3      236.66        236.78          bid_ask_mid                        5.3                bid_ask_mid                    True         -1035.0                  -7.83         91.67               12              1.45         26.78           24.82                  38.75                 169.0           31.0               0.12                      ok
```

## Today's Closed Trades (2026-06-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ROST           92.86               14            1.40              2.35        239.12                38.75         0.612          pass              0.497             21.9                           0.311                5.88              0.612                                 ok            True                  False
  CSCO           93.10               29            0.75              0.64        120.83                43.07         0.555          pass              0.658             42.0                           0.240               -0.94             -0.510                                 ok            True                  False
   BKR           80.77               26            1.06              0.47         62.94                39.91         0.546          pass              0.363             60.5                           0.576               -0.79             -0.212                                 ok            True                  False
  CPRT           83.33               18            1.46              0.32         30.61                31.00         0.527          pass              0.292             32.3                           0.463               -6.25             -0.198                                 ok            True                  False
   TRI           80.00               20            1.15              0.66         81.13                63.37         0.643          pass              0.143              4.1                           0.252              -14.36             -1.178 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                2            1.68              0.29         24.27                26.17         0.635          pass              0.471              2.4                           0.234                3.32              0.754                                 ok           False                  False
  AMGN           85.71                7            1.48              3.68        353.62                28.14         0.578          pass              0.230              6.7                           0.122                6.32              0.630                                 ok           False                  False
   ADP           95.45               22            1.35              2.14        225.29                32.50         0.551          pass              0.598             21.1                           0.447               -4.53             -0.309            downtrend_blocked_slope           False                  False
  WDAY           86.49               37            0.92              0.84        130.44                70.45         0.550          pass              0.543             45.0                           0.494              -17.57             -1.884 downtrend_blocked_slope_and_streak           False                  False
   EXC           87.50               24            0.08              0.02         46.20                21.24         0.543          pass              0.634             95.5                           0.452                4.25              0.390                                 ok           False                  False
   WMT           89.47               38            0.17              0.14        120.98                34.65         0.515          pass              0.766             91.9                           0.699                5.45              0.592                                 ok           False                  False
  MDLZ           50.00                2            2.35              1.04         62.55                19.17         0.506          pass              0.072              7.2                           0.211                0.75              0.335                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260615160005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260615160005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260615160005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260615160005)

</details>
