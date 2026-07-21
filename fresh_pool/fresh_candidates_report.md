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
1. `AKUN-001-UNKNOWN-VLESS-WS-76MS` (url=224ms, nekobox=284ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=234ms, nekobox=229ms, status=yes)
3. `AKUN-003-090227-VLESS-WS-95MS` (url=222ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=226ms, nekobox=267ms, status=yes)
5. `AKUN-005-LEVIKOGJGFDD-VLESS-WS-109MS` (url=226ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=222ms, nekobox=258ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-108MS` (url=216ms, nekobox=284ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-115MS` (url=235ms, nekobox=263ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=227ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS` (url=233ms, nekobox=275ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-127MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-132MS` (url=258ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-128MS` (url=241ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-118MS` (url=263ms, status=HTTP 204)
16. `AKUN-016-ZOOM-VLESS-WS-134MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-174MS` (url=251ms, status=HTTP 204)
18. `AKUN-019-ORG-VLESS-WS-102MS` (url=264ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-134MS` (url=236ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-388MS` (url=851ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-391MS` (url=4793ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-397MS` (url=776ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-651MS` (url=1093ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-638MS` (url=1269ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-703MS` (url=1163ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
