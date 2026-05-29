# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 11:10:06 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$33,344.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$1,080.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 15180.0        35.25          37.95      477.34        476.58          bid_ask_mid                      37.95                bid_ask_mid                    True          1080.0                   7.66         97.22               36              0.69         45.69           53.77                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           95.45               22            2.15              1.82        120.11                85.20         0.600            pass              0.598             19.3                           0.283                2.03              1.003                                 ok            True                  False
   TXN          100.00               13            2.32              5.12        313.75                35.59         0.501            pass              0.492              7.2                           0.181                0.15              0.455                                 ok            True                  False
  INSM           72.22               36            1.00              0.76        108.05               111.11         0.770            pass              0.369             39.7                           0.333               -7.20             -0.374            downtrend_blocked_slope           False                  False
   AEP           77.78               18            0.39              0.35        127.61                25.60         0.590            pass              0.269             52.4                           0.371               -1.04              0.114                                 ok           False                  False
  REGN           89.19               37            0.29              1.26        620.98                44.05         0.547            pass              0.697             72.3                           0.372              -12.94             -1.052 downtrend_blocked_slope_and_streak           False                  False
   PEP           91.67               12            1.50              1.54        145.63                23.56         0.538            pass              0.432             17.9                           0.205               -3.08             -0.286            downtrend_blocked_slope           False                  False
 GOOGL           84.62               13            1.72              4.69        388.12                41.30         0.525            pass              0.289             31.3                           0.574               -4.40             -0.330            downtrend_blocked_slope           False                  False
  AMGN           89.66               29            0.43              1.02        336.04                27.03         0.520            pass              0.609             57.6                           0.423                0.40              0.275                                 ok           False                  False
  SBUX           90.91               11            1.33              0.94        100.35                16.60         0.511            pass              0.521             57.3                           0.330               -6.03             -0.729            downtrend_blocked_slope           False                  False
  GOOG           88.24               17            1.60              4.33        384.26                41.01         0.503            pass              0.422             35.0                           0.586               -4.34             -0.340            downtrend_blocked_slope           False                  False
  MCHP           90.00               30            0.61              0.41         95.86                39.01         0.487 below_threshold              0.535             28.9                           0.250               -1.14              0.309                                 ok           False                  False
   CSX           60.00               10            1.70              0.55         45.58                23.65         0.484 below_threshold              0.090             13.8                           0.228               -1.94             -0.010           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-29T11:10:06.165530-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T11:05:07.175398-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T11:00:03.169868-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:55:06.987208-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:50:02.163774-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:45:04.066585-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:40:02.188936-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:35:01.212926-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:30:02.245861-04:00 early_entry_1030         entry {"allocated_cash": 14100.0, "asset_type": "option", "contract_symbol": "SNPS260717C00470000", "contracts": 4, "early_entry_score": 0.826, "entry_mode": "early", "entry_option_price": 35.25, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 115.0, "option_spread_pct": 11.06, "option_volume": 67.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.401}
2026-05-29T10:25:01.208564-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529111006)

</details>
