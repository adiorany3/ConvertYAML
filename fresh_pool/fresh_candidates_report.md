# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=246ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=203ms, nekobox=261ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=247ms, nekobox=252ms, status=yes)
4. `AKUN-004-AMBYRE-NET-VLESS-WS-78MS` (url=218ms, nekobox=268ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=220ms, nekobox=176ms, status=no)
6. `AKUN-005-UNKNOWN-VLESS-WS-76MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS`
8. `AKUN-007-CLOUDWEBMANAGE-EU-FR-VLESS-WS-88MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS`
10. `AKUN-009-DIGITALOCEAN-VLESS-WS-82MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-83MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-DIGITALOCEAN-VLESS-WS-73MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-90MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-81MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-US-VLESS-WS-84MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-95MS` (url=261ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-77MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-MEDIUM-VLESS-WS-75MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-ADF-VLESS-WS-127MS` (url=209ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-152MS` (url=319ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-100MS` (url=212ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-106MS` (url=205ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-370MS` (url=784ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-375MS` (url=726ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
