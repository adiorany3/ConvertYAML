# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 16
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 22

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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=216ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=235ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-114MS` (url=203ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-119MS` (url=227ms, nekobox=251ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-121MS` (url=207ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-130MS` (url=219ms, nekobox=235ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-154MS` (url=220ms, nekobox=258ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-110MS` (url=210ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-274MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-287MS`
11. `AKUN-012-SPEEDTEST-VLESS-WS-298MS` (url=609ms, status=HTTP 204)
12. `AKUN-013-CONFLU-VLESS-WS-245MS` (url=505ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-279MS` (url=2625ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-286MS` (url=2622ms, status=HTTP 204)
15. `AKUN-018-CLOUDFLARE-VLESS-WS-406MS` (url=573ms, status=HTTP 204)
16. `AKUN-030-CLOUDFLARE-VLESS-WS-462MS` (url=1606ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
