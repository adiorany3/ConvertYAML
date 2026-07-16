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
1. `AKUN-001-UNKNOWN-VLESS-WS-68MS` (url=209ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=214ms, nekobox=252ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=218ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=204ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=223ms, nekobox=242ms, status=yes)
6. `AKUN-006-DIXONS-VLESS-WS-76MS` (url=213ms, nekobox=231ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, nekobox=246ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-62MS` (url=228ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=200ms, nekobox=254ms, status=yes)
10. `AKUN-010-466688-VLESS-WS-96MS`
11. `AKUN-012-ORG-VLESS-WS-92MS` (url=230ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-81MS` (url=224ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-93MS` (url=226ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=205ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-120MS` (url=231ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-91MS` (url=202ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-77MS` (url=221ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-211MS` (url=1707ms, status=HTTP 204)
19. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-227MS` (url=1695ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-245MS` (url=526ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-142MS` (url=227ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-245MS` (url=584ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-87MS` (url=231ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-411MS` (url=945ms, status=HTTP 204)
25. `AKUN-028-WEBEX-VLESS-WS-66MS` (url=219ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
