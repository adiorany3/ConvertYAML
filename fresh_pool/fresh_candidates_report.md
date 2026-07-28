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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-121MS` (url=255ms, nekobox=310ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-123MS` (url=261ms, nekobox=262ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-129MS` (url=280ms, nekobox=272ms, status=yes)
4. `AKUN-004-ORDAKBOT-VLESS-WS-129MS` (url=1600ms, nekobox=436ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-124MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-130MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-131MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-127MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-123MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-118MS`
11. `AKUN-010-MEDIUM-VLESS-WS-149MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-163MS` (url=281ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-122MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-171MS` (url=242ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-207MS` (url=270ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-173MS` (url=277ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-206MS` (url=339ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-178MS` (url=429ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-144MS` (url=771ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-332MS` (url=450ms, status=HTTP 204)
21. `AKUN-023-TANG-NET-VLESS-WS-384MS` (url=774ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-412MS` (url=824ms, status=HTTP 204)
23. `AKUN-026-DEV-VLESS-WS-491MS` (url=1084ms, status=HTTP 204)
24. `AKUN-027-SKK-VLESS-WS-169MS` (url=313ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-780MS` (url=1117ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
