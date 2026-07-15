# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 10:40:04 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$19,710.25`
- Equity: `$29,990.25`
- Realized PnL: `$19,085.25`
- Unrealized PnL: `$905.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                 10280.0        46.88           51.4      660.72        674.22          bid_ask_mid                       51.4                bid_ask_mid                    True           905.0                   9.65         81.82               22              1.27         53.38           51.29                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15        11.55       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           88.24               17            2.61              5.57        303.16                65.52         0.565          pass              0.335              4.0                           0.121               -0.16              0.229                                 ok            True                  False
  NXPI           85.19               27            1.35              2.69        282.72                58.07         0.561          pass              0.351             14.4                           0.195               -0.36              0.256                                 ok            True                  False
   CSX           87.50               16            0.90              0.31         49.79                19.08         0.559          pass              0.408             37.5                           0.600                4.08              0.354                                 ok            True                  False
   LIN          100.00               13            1.20              4.38        520.66                20.66         0.556          pass              0.556             26.9                           0.341               -0.51             -0.299                                 ok            True                  False
   ADI           86.96               23            1.91              5.26        390.50                55.85         0.555          pass              0.336              2.9                           0.040               -3.01              0.046                                 ok            True                  False
  QCOM           83.87               31            0.98              1.22        177.58                61.79         0.584          pass              0.373             23.9                           0.243               -4.56             -0.088           downtrend_blocked_streak           False                  False
  KLAC           75.00               12            4.48              7.22        227.28               109.33         0.581          pass              0.082              3.5                           0.135              -27.06             -2.117 downtrend_blocked_slope_and_streak           False                  False
  MCHP           96.00               25            2.17              1.32         86.54                68.63         0.562          pass              0.589             10.8                           0.184               -6.56             -0.294            downtrend_blocked_slope           False                  False
  AMAT           78.57               14            3.90             16.28        588.72                98.89         0.558          pass              0.085              0.8                           0.046              -20.82             -1.432 downtrend_blocked_slope_and_streak           False                  False
  ASML           93.75               32            1.04             12.90       1770.11                66.00         0.550          pass              0.572              1.1                           0.208              -11.67             -0.756            downtrend_blocked_slope           False                  False
  MPWR           76.00               25            2.81             27.09       1364.80                84.79         0.547          pass              0.194             13.1                           0.192               -3.23              0.103                                 ok           False                  False
   WBD           77.78                9            1.20              0.23         27.38                20.00         0.542          pass              0.090             12.0                           0.150                1.84              0.263                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-07-15T10:40:04.846319-04:00 early_entry_1040 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:35:02.734120-04:00 early_entry_1035 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:30:03.936476-04:00 early_entry_1030 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:25:06.040216-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:20:02.772383-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:15:05.965611-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:10:03.001163-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:05:02.748975-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:00:03.493578-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:00:03.493578-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "AAPL260821C00315000", "fill_price": 13.45, "pnl": 2090.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.45, "ticker": "AAPL"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715104004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715104004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715104004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715104004)

</details>
