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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=207ms, nekobox=262ms, status=yes)
2. `AKUN-002-NEXUSMODS-VLESS-WS-92MS` (url=214ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=235ms, nekobox=354ms, status=yes)
4. `AKUN-004-DIGITALOCEAN-VLESS-WS-96MS` (url=217ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=216ms, nekobox=246ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-87MS` (url=216ms, nekobox=245ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-99MS` (url=215ms, nekobox=244ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=221ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=244ms, nekobox=306ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-117MS` (url=273ms, nekobox=290ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-118MS` (url=256ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-88MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-TENCENT-VLESS-WS-114MS` (url=241ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-139MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-107MS` (url=322ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-108MS` (url=256ms, status=HTTP 204)
18. `AKUN-018-PUBLICDOMAINREGISTRY-NET-VLESS-WS-113MS` (url=211ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-133MS` (url=232ms, status=HTTP 204)
20. `AKUN-020-ILOVEZHENJIU-VLESS-WS-133MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-384MS` (url=775ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-397MS` (url=753ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-386MS` (url=1050ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-414MS` (url=876ms, status=HTTP 204)
25. `AKUN-025-GALAKTIKA-20201015-VLESS-WS-439MS` (url=5201ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
