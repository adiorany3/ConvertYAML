# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-115MS` (url=268ms, nekobox=278ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-122MS` (url=294ms, nekobox=286ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-124MS` (url=265ms, nekobox=279ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-133MS` (url=254ms, nekobox=339ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-135MS` (url=246ms, nekobox=288ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-124MS` (url=260ms, nekobox=269ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-131MS` (url=268ms, nekobox=317ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-126MS` (url=260ms, nekobox=306ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-139MS` (url=242ms, nekobox=296ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-142MS` (url=256ms, nekobox=279ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-153MS` (url=267ms, status=HTTP 204)
12. `AKUN-013-SKK-VLESS-WS-158MS` (url=329ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-131MS` (url=253ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-158MS` (url=288ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-200MS` (url=353ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-398MS` (url=803ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-397MS` (url=1889ms, status=HTTP 204)
18. `AKUN-020-LEVIKOGJGFDD-VLESS-WS-535MS` (url=2910ms, status=HTTP 204)
19. `AKUN-023-UNKNOWN-VLESS-WS-762MS` (url=1259ms, status=HTTP 204)
20. `AKUN-027-SUKARIO-VLESS-WS-724MS` (url=1163ms, status=HTTP 204)
21. `AKUN-030-UNKNOWN-VLESS-WS-791MS` (url=1254ms, status=HTTP 204)
22. `AKUN-032-CLOUDFLARE-VLESS-WS-819MS` (url=1860ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
