# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 15:00:05 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$606.99`
- Equity: `$13,548.63`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$-799.29`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback               REGN       2026-04-16                   0      9     6720.93                 6731.64       746.77         747.96      746.77        747.96           10.71                   0.16         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
   HON     option         option HON260515C00240000       2026-04-15                   1     18     7020.00                 6210.00         3.90           3.45      231.34        229.79         -810.00                 -11.54         100.0               22              0.82         27.49           28.47                  23.78                2322.0          110.0               0.05                                       ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               31            0.79              4.18        752.14                24.02            True
   HON          100.00               19            1.03              1.68        231.47                23.34            True
  MRVL           97.62               42            0.52              0.49        134.39                70.04            True
   WDC           96.97               33            1.42              3.62        363.45                79.90            True
   AEP           95.45               22            0.62              0.58        134.14                19.19            True
  ROST           90.91               11            1.53              2.40        223.12                24.88            True
  ORLY           87.88               33            0.82              0.54         93.37                23.50            True
  KLAC           87.50               32            1.21             14.83       1741.75                51.26            True
  GILD           86.96               23            0.94              0.92        139.37                21.89            True
  VRTX           86.36               22            1.71              5.28        439.44                27.87            True
 GOOGL           84.62               39            0.54              1.28        336.57                37.85            True
   EXC           84.62               13            1.02              0.34         47.73                22.11            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-04-16T15:00:05.944863-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-16T14:55:06.168816-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-16T14:50:02.253743-04:00  entry_1500        entry {"allocated_cash": 6720.93, "asset_type": "share", "contract_symbol": "REGN", "contracts": 9, "entry_option_price": 746.77, "execution_mode": "share_fallback", "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 15.18, "option_volume": 3.0, "success_rate": 100.0, "ticker": "REGN"}
2026-04-16T14:40:06.525547-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-16T14:35:06.445500-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-16T14:30:06.437775-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-16T14:25:06.447570-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-16T14:10:06.435946-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-16T14:05:06.594374-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-16T14:00:06.440718-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416150005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416150005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416150005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416150005)

</details>
