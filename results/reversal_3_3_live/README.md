# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 09:30:01 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$4,018.50`
- Equity: `$34,003.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$400.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   2      3     13410.0                 13785.0        44.70          45.95      510.62        506.37     last_price_stale                        NaN                unavailable                   False           375.0                   2.80         97.14               35              0.50         52.16             0.0                  43.23                 154.0           10.0               0.12                      ok
  CDNS     option         option CDNS260618C00330000       2026-05-14                   1      5     16175.0                 16200.0        32.35          32.40      352.55        350.71     last_price_stale                        NaN                unavailable                   False            25.0                   0.15         97.30               37              0.56         47.46             0.0                  37.69                2023.0           40.0               0.10                      ok
```

## Today's Closed Trades (2026-05-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.00               10            2.46              5.31        305.89                67.99         0.695          pass              0.432             32.1                           0.444                7.51              0.995                                 ok            True                  False
  FTNT           97.37               38            0.66              0.56        121.62                71.29         0.606          pass              0.889             80.4                           0.540               40.29              3.895                                 ok            True                  False
  CSCO           92.31               26            0.69              0.56        115.29                49.80         0.604          pass              0.735             80.0                           0.694               24.91              2.233                                 ok            True                  False
 GOOGL           86.36               22            1.29              3.62        399.52                40.65         0.571          pass              0.426             39.7                           0.498                2.65              0.311                                 ok            True                  False
  GOOG           85.19               27            1.08              3.00        395.89                40.76         0.553          pass              0.447             46.6                           0.460                2.52              0.308                                 ok            True                  False
  SNPS           97.14               35            0.79              2.83        508.81                41.57         0.543          pass              0.800             59.6                           0.410                3.47              0.333                                 ok            True                  False
  CDNS           97.30               37            0.61              1.50        352.20                37.94         0.525          pass              0.831             66.2                           0.613                2.86              0.204                                 ok            True                   True
  SBUX           96.67               30            0.92              0.69        106.11                33.04         0.520          pass              0.675             30.0                           0.380               -0.45              0.070                                 ok            True                  False
  NXPI           75.00               16            2.68              5.52        291.81                90.16         0.714          pass              0.154             14.1                           0.165               -3.03             -0.050                                 ok           False                  False
  INSM           72.22               36            1.14              0.92        115.22               110.45         0.685          pass              0.353             37.1                           0.247              -14.23             -2.163 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00                5            5.80              4.71        113.91               111.79         0.610          pass              0.519             19.3                           0.276                9.62              1.671                                 ok           False                  False
  GEHC           73.68               38            0.59              0.26         62.56                57.53         0.574          pass              0.474             76.7                           0.512                2.08              0.251                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-15T00:00:05.036344-04:00     data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 92}
2026-05-14T15:10:04.841035-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T15:05:08.308131-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T15:00:08.187447-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T14:55:08.383255-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T14:50:07.158439-04:00       entry_1500  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T14:50:07.158439-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-14", "training_samples": 5049, "window": 5}
2026-05-14T11:37:47.828844-04:00 early_entry_1135  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T10:50:02.088724-04:00 early_entry_1050  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T10:06:24.763261-04:00 early_entry_1005          entry {"allocated_cash": 16175.0, "asset_type": "option", "contract_symbol": "CDNS260618C00330000", "contracts": 5, "early_entry_score": 0.833, "entry_mode": "early", "entry_option_price": 32.35, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2023.0, "option_spread_pct": 10.2, "option_volume": 40.0, "success_rate": 97.3, "ticker": "CDNS", "timing_score": 0.51}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515093001)

</details>
