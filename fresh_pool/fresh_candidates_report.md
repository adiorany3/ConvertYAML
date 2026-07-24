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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-74MS` (url=230ms, nekobox=315ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=232ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=206ms, nekobox=263ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=221ms, nekobox=255ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=222ms, nekobox=350ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=222ms, nekobox=231ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-105MS` (url=222ms, nekobox=245ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=221ms, nekobox=251ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-108MS` (url=216ms, nekobox=231ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS` (url=228ms, nekobox=252ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-96MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-113MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-146MS` (url=272ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-143MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-132MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-179MS` (url=247ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-103MS` (url=201ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-232MS` (url=550ms, status=HTTP 204)
20. `AKUN-020-PMBET-NET-VLESS-WS-243MS` (url=3340ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-114MS` (url=250ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-153MS` (url=233ms, status=HTTP 204)
23. `AKUN-024-ZVC-VLESS-WS-74MS` (url=234ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-140MS` (url=202ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-283MS` (url=523ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
