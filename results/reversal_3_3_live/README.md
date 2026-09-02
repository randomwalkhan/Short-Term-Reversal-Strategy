# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 09:50:01 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$23,958.10`
- Equity: `$46,638.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$-1,080.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 22680.0         1.65           1.58       32.33         32.13          bid_ask_mid                       1.58                bid_ask_mid                    True         -1080.0                  -4.55          87.5               16              1.99         38.72           46.97                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.33               36            1.11              0.97        124.46                86.77         0.605          pass              0.513             63.4                           0.611               18.46              1.590                       ok            True                  False
  PAYX          100.00               16            1.12              0.99        125.22                25.34         0.521          pass              0.643             50.4                           0.489                1.41              0.231                       ok            True                  False
  CSCO           89.19               37            0.58              0.44        109.55                36.37         0.517          pass              0.519             14.2                           0.177               -1.31             -0.065                       ok            True                  False
  SNPS           90.48               42            0.64              1.87        414.02                58.04         0.509          pass              0.737             68.8                           0.456                2.72              0.871                       ok            True                  False
    ZS          100.00               33            1.85              2.31        177.38                60.79         0.509          pass              0.718             38.0                           0.339               -5.16              0.106                       ok            True                  False
  AVGO           82.35               34            0.65              1.69        368.96                36.24         0.502          pass              0.429             52.1                           0.463                1.32              0.217                       ok            True                  False
  MNST           88.24               17            1.14              0.36         44.84               424.41         1.000          pass              0.437             23.7                           0.273               -6.23             -0.715  downtrend_blocked_slope           False                  False
  ABNB           94.59               37            0.23              0.29        182.42                64.48         0.655          pass              0.884             83.0                           0.591               -2.29             -0.251  downtrend_blocked_slope           False                  False
   APP           72.09               43            0.47              1.03        311.30                85.96         0.646          pass              0.492             75.8                           0.638               -0.17              0.202                       ok           False                  False
   WDC           81.82               33            0.98              3.08        449.12                82.26         0.637          pass              0.447             60.6                           0.592               -3.47             -0.241 downtrend_blocked_streak           False                  False
  MCHP           89.19               37            0.41              0.20         71.32                59.53         0.601          pass              0.719             77.9                           0.564               -7.18             -0.621  downtrend_blocked_slope           False                  False
  CRWD           78.57               14            3.30              4.96        212.94                87.98         0.570          pass              0.140             18.9                           0.224                3.15              1.525                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                                                              detail
2026-09-02T09:40:05.355091-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:35:05.293548-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:30:01.390795-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:25:06.105664-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:20:01.375849-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T00:00:06.180126-04:00 data_refresh data_refresh                                                                                                                                                                                                       {'saved': 93}
2026-09-01T15:10:01.952718-04:00   entry_1500 slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-01T15:05:02.102329-04:00   entry_1500 slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-01T15:00:06.883715-04:00   entry_1500 slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-01T14:55:03.896264-04:00   entry_1500 slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902095001)

</details>
