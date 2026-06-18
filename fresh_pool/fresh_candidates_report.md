# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-104MS` (url=266ms, nekobox=310ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-117MS` (url=293ms, nekobox=320ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-146MS` (url=296ms, nekobox=289ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-135MS` (url=269ms, nekobox=291ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-129MS` (url=280ms, nekobox=347ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-151MS` (url=268ms, nekobox=304ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS` (url=255ms, nekobox=306ms, status=yes)
8. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-160MS` (url=275ms, nekobox=325ms, status=yes)
9. `AKUN-009-CALMLOUD-VLESS-WS-341MS` (url=2403ms, nekobox=483ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-319MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-339MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-405MS` (url=703ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-399MS` (url=699ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-354MS` (url=3103ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-406MS` (url=730ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-458MS` (url=1016ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-247MS` (url=444ms, status=HTTP 204)
18. `AKUN-025-BIGCOMMERCE-VLESS-WS-533MS` (url=950ms, status=HTTP 204)
19. `AKUN-027-UNKNOWN-VLESS-WS-607MS` (url=843ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-623MS` (url=1026ms, status=HTTP 204)
21. `AKUN-034-CLOUDFLARE-VLESS-WS-702MS` (url=4218ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
