# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 11:15:06 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$18,164.25`
- Equity: `$33,324.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$1,060.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 15160.0        35.25           37.9      477.34        475.27          bid_ask_mid                       37.9                bid_ask_mid                    True          1060.0                   7.52         97.22               36              0.69         45.69           50.43                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           96.15               26            1.74              1.47        120.26                85.20         0.601            pass              0.672             35.0                           0.347                2.47              1.022                                 ok            True                  False
  MDLZ           92.86               14            1.14              0.50         62.18                12.98         0.514            pass              0.574             51.0                           0.368                1.16              0.192                                 ok            True                  False
   TXN          100.00               14            2.06              4.55        314.00                35.59         0.511            pass              0.531             17.6                           0.221                0.42              0.467                                 ok            True                  False
  INSM           72.22               36            1.06              0.80        108.03               111.11         0.767            pass              0.357             35.8                           0.304               -7.27             -0.377            downtrend_blocked_slope           False                  False
   AEP           75.00               16            0.49              0.44        127.57                25.60         0.593            pass              0.219             40.0                           0.284               -1.14              0.110                                 ok           False                  False
  MNST           95.65               46            0.06              0.04         87.97                49.61         0.559            pass              0.939             94.4                           0.506                2.46              0.191                                 ok           False                  False
  REGN           88.57               35            0.46              2.01        620.66                44.05         0.548            pass              0.618             55.9                           0.281              -13.09             -1.060 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.91               11            1.58              1.61        145.60                23.56         0.539            pass              0.393             14.0                           0.149               -3.15             -0.289            downtrend_blocked_slope           False                  False
 GOOGL           84.62               13            1.70              4.65        388.14                41.30         0.527            pass              0.291             31.9                           0.604               -4.38             -0.330            downtrend_blocked_slope           False                  False
  AMGN           89.29               28            0.49              1.16        335.98                27.03         0.523            pass              0.574             51.5                           0.369                0.33              0.272                                 ok           False                  False
  SBUX           90.00               10            1.42              1.00        100.32                16.60         0.512            pass              0.482             54.6                           0.286               -6.11             -0.733            downtrend_blocked_slope           False                  False
  GOOG           88.89               18            1.57              4.25        384.30                41.01         0.499 below_threshold              0.449             36.4                           0.621               -4.31             -0.339            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-29T11:15:06.204511-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T11:10:06.165530-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T11:05:07.175398-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T11:00:03.169868-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:55:06.987208-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:50:02.163774-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:45:04.066585-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:40:02.188936-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:35:01.212926-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:30:02.245861-04:00 early_entry_1030         entry {"allocated_cash": 14100.0, "asset_type": "option", "contract_symbol": "SNPS260717C00470000", "contracts": 4, "early_entry_score": 0.826, "entry_mode": "early", "entry_option_price": 35.25, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 115.0, "option_spread_pct": 11.06, "option_volume": 67.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.401}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529111506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529111506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529111506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529111506)

</details>
