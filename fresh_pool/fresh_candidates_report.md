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
1. `AKUN-001-ZVC-VLESS-WS-90MS` (url=230ms, nekobox=237ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-116MS` (url=221ms, nekobox=237ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-135MS` (url=219ms, nekobox=254ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-127MS`
5. `AKUN-005-DEV-VLESS-WS-139MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS`
7. `AKUN-008-DEV-VLESS-WS-134MS` (url=217ms, nekobox=225ms, status=no)
8. `AKUN-007-UNKNOWN-VLESS-WS-131MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-137MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-126MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS`
12. `AKUN-013-UNKNOWN-VLESS-WS-119MS` (url=243ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-123MS` (url=232ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-161MS` (url=262ms, status=HTTP 204)
15. `AKUN-016-DIGITALOCEAN-VLESS-WS-105MS` (url=229ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-122MS` (url=220ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-113MS` (url=233ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-111MS` (url=235ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-132MS` (url=216ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-262MS` (url=332ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-287MS` (url=541ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-382MS` (url=778ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-375MS` (url=793ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-411MS` (url=851ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-391MS` (url=791ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
