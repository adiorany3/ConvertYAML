# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=207ms, nekobox=244ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=217ms, nekobox=228ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-93MS` (url=204ms, nekobox=219ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS`
7. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-92MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-132MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-276MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-279MS` (url=584ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-307MS` (url=712ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-268MS` (url=2383ms, status=HTTP 204)
15. `AKUN-018-CLOUDFLARE-VLESS-WS-252MS` (url=549ms, status=HTTP 204)
16. `AKUN-019-JISON-VLESS-WS-345MS` (url=683ms, status=HTTP 204)
17. `AKUN-022-CLOUDFLARE-VLESS-WS-440MS` (url=750ms, status=HTTP 204)
18. `AKUN-030-UNKNOWN-VLESS-WS-508MS` (url=853ms, status=HTTP 204)
19. `AKUN-033-SPEEDTEST-VLESS-WS-223MS` (url=393ms, status=HTTP 204)
20. `AKUN-034-SPEEDTEST-VLESS-WS-433MS` (url=823ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
