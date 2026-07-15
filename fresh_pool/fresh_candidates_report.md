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
1. `AKUN-001-UNKNOWN-VLESS-WS-97MS` (url=247ms, nekobox=275ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-96MS` (url=208ms, nekobox=247ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-104MS` (url=217ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-104MS` (url=243ms, nekobox=271ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-94MS` (url=255ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS` (url=260ms, nekobox=278ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS` (url=260ms, nekobox=291ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=232ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS` (url=444ms, nekobox=279ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=221ms, nekobox=268ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-126MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-105MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-PUBLICDOMAINREGISTRY-NET-VLESS-WS-122MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-151MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=234ms, status=HTTP 204)
17. `AKUN-017-1PASSWORD-VLESS-WS-145MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-108MS` (url=236ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-138MS` (url=217ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-182MS` (url=1204ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-136MS` (url=228ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-127MS` (url=235ms, status=HTTP 204)
23. `AKUN-023-466688-VLESS-WS-217MS` (url=276ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-140MS` (url=247ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-107MS` (url=227ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
