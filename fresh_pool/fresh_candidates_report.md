# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-99MS` (url=233ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-113MS` (url=217ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-124MS` (url=222ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-109MS` (url=201ms, nekobox=273ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-113MS` (url=246ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-119MS` (url=226ms, nekobox=245ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-113MS` (url=232ms, nekobox=258ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-130MS` (url=259ms, nekobox=247ms, status=yes)
9. `AKUN-009-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-114MS` (url=207ms, nekobox=277ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS` (url=230ms, nekobox=275ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-104MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-110MS` (url=287ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-131MS` (url=255ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-375MS` (url=785ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-364MS` (url=756ms, status=HTTP 204)
16. `AKUN-016-MICROSOFT-VLESS-WS-403MS` (url=847ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-411MS` (url=828ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-398MS` (url=828ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-399MS` (url=807ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-404MS` (url=777ms, status=HTTP 204)
21. `AKUN-028-UNKNOWN-VLESS-WS-753MS` (url=1227ms, status=HTTP 204)
22. `AKUN-032-CLOUDFLARE-VLESS-WS-864MS` (url=1407ms, status=HTTP 204)
23. `AKUN-034-CLOUDFLARE-VLESS-WS-666MS` (url=1104ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
