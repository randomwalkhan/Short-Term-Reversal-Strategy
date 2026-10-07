# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 10:15:04 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$53,034.30`
- Equity: `$103,359.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-1,787.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 50325.0         9.48           9.15      160.14        158.99          bid_ask_mid                       9.15                bid_ask_mid                    True         -1787.5                  -3.43         83.33               12               2.4         42.26           45.35                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           80.65               31            0.91              3.21        503.79                54.22         0.559          pass              0.290             25.6                           0.242               21.19              2.320                                 ok            True                  False
  UPRO           91.67               12            1.89              2.06        155.53                30.90         0.555          pass              0.394              4.8                           0.137                2.10              0.302                                 ok            True                  False
   KDP           95.00               20            0.92              0.20         31.04                26.61         0.534          pass              0.540              6.6                           0.108               -2.18             -0.191                                 ok            True                  False
  MPWR           81.25               16            3.23             33.32       1459.41                53.62         0.526          pass              0.192             22.0                           0.309                5.37              0.943                                 ok            True                  False
   XEL           86.36               22            0.52              0.27         72.62                18.69         0.524          pass              0.439             45.7                           0.322                2.39              0.385                                 ok            True                  False
  SHOP           86.49               37            1.01              1.16        163.94                52.70         0.503          pass              0.541             45.8                           0.591               14.36              1.482                                 ok            True                  False
  DASH           80.00               25            1.90              2.57        192.52                42.81         0.503          pass              0.166              5.2                           0.169                0.36              0.192                                 ok            True                  False
  QCOM           85.71               28            1.19              1.50        180.39                56.22         0.586          pass              0.475             48.1                           0.664               -9.31             -1.038 downtrend_blocked_slope_and_streak           False                  False
  META           58.33               12            2.18             11.26        734.05                55.45         0.582          pass              0.087              5.2                           0.161               -2.86             -0.338            downtrend_blocked_slope           False                  False
   CEG           77.78                9            2.62              5.52        298.04                58.89         0.576          pass              0.189             43.7                           0.550               10.85              0.975                                 ok           False                  False
  CSCO           85.71               28            0.40              0.33        117.80                34.67         0.558          pass              0.516             62.7                           0.662               10.80              1.111                                 ok           False                  False
  SOXL           79.17               24            5.75              6.62        161.42               111.15         0.552          pass              0.228             26.4                           0.624                5.85              1.196                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-07T10:15:04.665736-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:10:02.695128-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:05:05.843456-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:00:06.491610-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T00:00:06.148407-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-10-06T15:10:04.494335-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T15:05:04.280902-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T15:00:04.457281-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T14:55:01.305987-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T14:50:04.366747-04:00       entry_1500              entry {"allocated_cash": 52112.5, "asset_type": "option", "contract_symbol": "ABNB261120C00160000", "contracts": 55, "early_entry_score": 0.219, "entry_mode": "regular", "entry_option_price": 9.475, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 310.0, "option_spread_pct": 5.8, "option_volume": 20.0, "success_rate": 83.33, "ticker": "ABNB", "timing_score": 0.529}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007101504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007101504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007101504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007101504)

</details>
